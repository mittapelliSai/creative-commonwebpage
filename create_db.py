from app import app, db, License, BlogPost
from datetime import datetime

with app.app_context():
    db.create_all()

    # Add licenses
    licenses = [
        License(
            name="Attribution",
            abbreviation="CC BY",
            description="This license lets others distribute, remix, adapt, and build upon your work, even commercially, as long as they credit you for the original creation.",
            allows_commercial=True,
            allows_derivatives=True,
            requires_sharealike=False,
            requires_attribution=True,
            icon="by.svg",
            legal_code_url="https://creativecommons.org/licenses/by/4.0/legalcode",
            deed_url="https://creativecommons.org/licenses/by/4.0/"
        ),
        License(
            name="Attribution-ShareAlike",
            abbreviation="CC BY-SA",
            description="This license lets others remix, adapt, and build upon your work even for commercial purposes, as long as they credit you and license their new creations under the identical terms.",
            allows_commercial=True,
            allows_derivatives=True,
            requires_sharealike=True,
            requires_attribution=True,
            icon="by-sa.svg",
            legal_code_url="https://creativecommons.org/licenses/by-sa/4.0/legalcode",
            deed_url="https://creativecommons.org/licenses/by-sa/4.0/"
        ),
        License(
            name="Attribution-NonCommercial",
            abbreviation="CC BY-NC",
            description="This license lets others remix, adapt, and build upon your work non-commercially, and although their new works must also acknowledge you and be non-commercial, they don't have to license their derivative works on the same terms.",
            allows_commercial=False,
            allows_derivatives=True,
            requires_sharealike=False,
            requires_attribution=True,
            icon="by-nc.svg",
            legal_code_url="https://creativecommons.org/licenses/by-nc/4.0/legalcode",
            deed_url="https://creativecommons.org/licenses/by-nc/4.0/"
        ),
        License(
            name="Attribution-NoDerivatives",
            abbreviation="CC BY-ND",
            description="This license allows for redistribution, commercial and non-commercial, as long as it is passed along unchanged and in whole, with credit to you.",
            allows_commercial=True,
            allows_derivatives=False,
            requires_sharealike=False,
            requires_attribution=True,
            icon="by-nd.svg",
            legal_code_url="https://creativecommons.org/licenses/by-nd/4.0/legalcode",
            deed_url="https://creativecommons.org/licenses/by-nd/4.0/"
        ),
        License(
            name="Attribution-NonCommercial-ShareAlike",
            abbreviation="CC BY-NC-SA",
            description="This license lets others remix, adapt, and build upon your work non-commercially, as long as they credit you and license their new creations under the identical terms.",
            allows_commercial=False,
            allows_derivatives=True,
            requires_sharealike=True,
            requires_attribution=True,
            icon="by-nc-sa.svg",
            legal_code_url="https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode",
            deed_url="https://creativecommons.org/licenses/by-nc-sa/4.0/"
        ),
        License(
            name="Attribution-NonCommercial-NoDerivatives",
            abbreviation="CC BY-NC-ND",
            description="This license is the most restrictive of our six main licenses, only allowing others to download your works and share them with others as long as they credit you, but they can't change them in any way or use them commercially.",
            allows_commercial=False,
            allows_derivatives=False,
            requires_sharealike=False,
            requires_attribution=True,
            icon="by-nc-nd.svg",
            legal_code_url="https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode",
            deed_url="https://creativecommons.org/licenses/by-nc-nd/4.0/"
        )
    ]

    db.session.add_all(licenses)

    # Add blog posts
    posts = [
        BlogPost(
            title="Introducing CC Signals: A New Social Contract for the Age of AI",
            content="Creative Commons (CC) today announces the public kickoff of the CC signals project, a new preference signals framework designed to increase reciprocity and sustain a creative commons in the age of AI. The development of CC signals represents a major step forward in how creators can express their preferences about how their works are used in AI systems.",
            author="Creative Commons",
            date=datetime(2025, 3, 15),
            category="Licenses & Tools, Policy",
            featured=True,
            license_info="CC Signals © 2025 by Creative Commons is licensed under CC BY 4.0"
        ),
        BlogPost(
            title="Understanding CC Licenses and AI Training: A Legal Primer",
            content="This article provides a comprehensive overview of how Creative Commons licenses interact with AI training data, addressing common questions and concerns from the community about the use of CC-licensed works in machine learning.",
            author="Sarah Hinchliff Pearson",
            date=datetime(2025, 2, 28),
            category="Policy",
            featured=True,
            license_info="CC BY 4.0"
        ),
        BlogPost(
            title="The Next Chapter: Strengthening the Creative Commons Community Together",
            content="As Creative Commons enters its third decade, we're reflecting on how our community has grown and evolved, and how we can continue to support the commons in an era of rapid technological change.",
            author="Jocelyn Miyara",
            date=datetime(2025, 2, 15),
            category="Community",
            featured=True,
            license_info="CC BY 4.0"
        ),
        BlogPost(
            title="CC @ SXSW: Protecting the Commons in the Age of AI",
            content="A recap of Creative Commons' participation at SXSW 2025, where we led discussions about maintaining a healthy digital commons in the face of challenges posed by generative AI systems.",
            author="Anna Tumasdottir, Jocelyn Miyara",
            date=datetime(2025, 3, 5),
            category="Events, Policy",
            featured=False,
            license_info="CC BY 4.0"
        )
    ]

    db.session.add_all(posts)
    db.session.commit()
    print("Database initialized with sample data.")