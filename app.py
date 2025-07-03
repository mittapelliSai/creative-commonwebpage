
from flask import Flask, render_template, request, redirect, url_for
from flask import request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models must be defined before creating tables
class License(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    abbreviation = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    allows_commercial = db.Column(db.Boolean, default=False)
    allows_derivatives = db.Column(db.Boolean, default=False)
    requires_sharealike = db.Column(db.Boolean, default=False)
    requires_attribution = db.Column(db.Boolean, default=True)
    icon = db.Column(db.String(50))
    legal_code_url = db.Column(db.String(200))
    deed_url = db.Column(db.String(200))

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(50))
    featured = db.Column(db.Boolean, default=False)
    image_url = db.Column(db.String(200))
    license_info = db.Column(db.String(100))
    
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    name = db.Column(db.String(80))  # Optional
    date_subscribed = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    source = db.Column(db.String(50))  # Where they subscribed from
    

# Create tables before first request
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    featured_posts = BlogPost.query.filter_by(featured=True).order_by(BlogPost.date.desc()).limit(3).all()
    licenses = License.query.all()
    return render_template('index.html', 
                         featured_posts=featured_posts,
                         licenses=licenses)

@app.route('/who-we-are')
def who_we_are():
    return render_template('who_we_are.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/licenses')
def licenses():
    return render_template('licenses.html', licenses=License.query.all())

@app.route('/license/<abbr>')
def license_detail(abbr):
    license = License.query.filter_by(abbreviation=abbr).first_or_404()
    return render_template(f'licenses/{abbr.lower()}.html', license=license)

@app.route('/choose-license', methods=['GET', 'POST'])
def choose_license():
    if request.method == 'POST':
        commercial = request.form.get('commercial') == 'on'
        derivatives = request.form.get('derivatives') == 'on'
        sharealike = request.form.get('sharealike') == 'on'
        
        if commercial:
            if derivatives:
                license = License.query.filter_by(abbreviation='CC BY-SA').first() if sharealike else License.query.filter_by(abbreviation='CC BY').first()
            else:
                license = License.query.filter_by(abbreviation='CC BY-ND').first()
        else:
            if derivatives:
                license = License.query.filter_by(abbreviation='CC BY-NC-SA').first() if sharealike else License.query.filter_by(abbreviation='CC BY-NC').first()
            else:
                license = License.query.filter_by(abbreviation='CC BY-NC-ND').first()
        
        return redirect(url_for('license_detail', abbr=license.abbreviation))
    
    return render_template('choose_license.html')

@app.route('/blog')
def blog():
    posts = BlogPost.query.order_by(BlogPost.date.desc()).all()
    return render_template('blog.html', posts=posts)

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('blog_post.html', post=post)

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    
    # Basic validation
    if not email or '@' not in email:
        flash('Please enter a valid email address', 'error')
        return redirect(request.referrer)
    
    # Check if email already exists
    existing = Subscriber.query.filter_by(email=email).first()
    if existing:
        flash('This email is already subscribed', 'info')
        return redirect(request.referrer)
    
    # Create new subscriber
    new_subscriber = Subscriber(
        email=email,
        source=request.referrer  # Track where they subscribed from
    )
    
    try:
        db.session.add(new_subscriber)
        db.session.commit()
        flash('Thank you for subscribing!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('An error occurred. Please try again.', 'error')
    
    return redirect(request.referrer)


if __name__ == '__main__':
    app.run(debug=True)