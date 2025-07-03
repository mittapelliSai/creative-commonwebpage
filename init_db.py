from app import app, db, License, BlogPost
from datetime import datetime

def initialize_data():
    with app.app_context():
        # Add licenses
        licenses = [
            License(
                name="Attribution",
                abbreviation="CC BY",
                description="This license lets others distribute, remix, adapt, and build upon your work, even commercially...",
                allows_commercial=True,
                allows_derivatives=True,
                requires_sharealike=False,
                requires_attribution=True,
                icon="by.svg",
                legal_code_url="https://creativecommons.org/licenses/by/4.0/legalcode",
                deed_url="https://creativecommons.org/licenses/by/4.0/"
            ),
            # Add other licenses...
        ]
        
        # Add blog posts
        posts = [
            BlogPost(
                title="Introducing CC Signals...",
                content="Creative Commons (CC) today announces...",
                author="Creative Commons",
                date=datetime(2025, 3, 15),
                category="Licenses & Tools, Policy",
                featured=True,
                license_info="CC BY 4.0"
            ),
            # Add other posts...
        ]
        
        db.session.add_all(licenses)
        db.session.add_all(posts)
        db.session.commit()
        print("Database initialized successfully!")

if __name__ == '__main__':
    initialize_data()