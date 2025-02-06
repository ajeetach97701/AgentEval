from langchain.schema import Document


# primary_colors_document = Document(
#     page_content="""
#     Primary Colors are colors that cannot be made by mixing other colors together. These colors are the building blocks for all other colors.
    
#     The primary colors are:
#     - **Red**: A strong, warm color associated with energy, passion, and action.
#     - **Blue**: A cool color associated with calmness, stability, and trust.
#     - **Yellow**: A bright color associated with optimism, happiness, and creativity.

#     These three colors form the basis for creating secondary and tertiary colors through mixing.
#     """,
#     metadata={
#         "topic": "Primary Colors",
#         "category": "Color Theory",
#         "keywords": ["red", "blue", "yellow", "primary colors"]
#     }
# )


# secondary_colors_document = Document(
#     page_content="""
#     Secondary Colors are formed by mixing two primary colors together. They provide a wide range of hues and enrich the color spectrum.

#     The secondary colors are:
#     - **Green**: Formed by mixing blue and yellow, it symbolizes nature, growth, and harmony.
#     - **Orange**: Formed by mixing red and yellow, it represents energy, warmth, and enthusiasm.
#     - **Purple**: Formed by mixing red and blue, it signifies royalty, luxury, and creativity.

#     These colors are essential for creating a balanced color palette.
#     """,
#     metadata={
#         "topic": "Secondary Colors",
#         "category": "Color Theory",
#         "keywords": ["green", "orange", "purple", "secondary colors"]
#     }
# )

# color_psychology_document = Document(
#     page_content="""
#     Color Psychology explores how different colors can affect human emotions and behavior. Colors can evoke psychological responses and influence moods.

#     Key psychological effects of colors:
#     - **Red**: Stimulates energy, passion, and urgency. Often used to grab attention.
#     - **Blue**: Creates a sense of calm, trust, and stability. It's widely used in corporate settings.
#     - **Yellow**: Represents optimism, happiness, and warmth. It can also increase concentration.
#     - **Green**: Evokes balance, calmness, and health. It's associated with nature and tranquility.

#     Understanding color psychology is crucial in design, marketing, and branding to influence consumer behavior.
#     """,
#     metadata={
#         "topic": "Color Psychology",
#         "category": "Psychological Impact",
#         "keywords": ["red", "blue", "yellow", "green", "psychology"]
#     }
# )

# color_harmonies_document = Document(
#     page_content="""
#     Color Harmony is the concept of combining colors in a way that is visually pleasing. There are several common types of color harmonies:

#     - **Complementary Colors**: Colors that are opposite each other on the color wheel (e.g., red and green).
#     - **Analogous Colors**: Colors that are next to each other on the color wheel (e.g., blue, blue-green, and green).
#     - **Triadic Colors**: Three colors that are evenly spaced on the color wheel (e.g., red, yellow, and blue).
#     - **Monochromatic Colors**: Variations of one hue, with different levels of saturation and lightness.

#     Color harmony helps to create balanced and visually appealing designs.
#     """,
#     metadata={
#         "topic": "Color Harmonies",
#         "category": "Design Principles",
#         "keywords": ["complementary", "analogous", "triadic", "monochromatic", "color harmony"]
#     }
# )

# docs = [primary_colors_document, secondary_colors_document, color_psychology_document, color_harmonies_document]




from langchain.schema import Document

# First Document object for the membership offer
document_1 = Document(
    page_content="""
    Available Membership Offers:
    
    1. **New Year Offer:**
    - **Monthly Membership (Auto-renewable):** 235 SAR (reduced from 358 SAR). No additional joining fee for a limited period. This membership has auto-renew, but you can cancel the auto-renewal option after one month.
    - **3-Month Membership:** 525 SAR (reduced from 949 SAR) with no joining fees.
    - **6-Month Membership:** 1230 SAR (reduced from 1599 SAR) with an additional 50 SAR joining fee.
    - **12-Month Membership:** 1960 SAR (reduced from 2499 SAR) with an additional 50 SAR joining fee.
    """,
    metadata={
        "offer_details": {
            "New Year Offer": {
                "Monthly Membership (Auto-renewable)": {
                    "price": "235 SAR",
                    "original_price": "358 SAR",
                    "joining_fee": "None",
                    "auto_renewal": "Yes",
                    "note": "Can cancel auto-renewal after one month"
                },
                "3-Month Membership": {
                    "price": "525 SAR",
                    "original_price": "949 SAR",
                    "joining_fee": "None"
                },
                "6-Month Membership": {
                    "price": "1230 SAR",
                    "original_price": "1599 SAR",
                    "joining_fee": "50 SAR"
                },
                "12-Month Membership": {
                    "price": "1960 SAR",
                    "original_price": "2499 SAR",
                    "joining_fee": "50 SAR"
                }
            }
        },
        "important_notes": [
            "Members must use the Active app for access.",
            "Members must be at least 18 years old to join."
        ],
        "contact_info": "Feel free to ask if you have any specific questions about offers or promotions"
    }
)

# Second Document object for the important notes
document_2 = Document(
    page_content="""
    Important Notes:
    - Members must use the Active app for access.
    - Members must be at least 18 years old to join.
    
    If you have any specific questions about offers or promotions, feel free to ask!
    """,
    metadata={
        "important_notes": [
            "Members must use the Active app for access.",
            "Members must be at least 18 years old to join."
        ],
        "contact_info": "Feel free to ask if you have any specific questions about offers or promotions"
    }
)


docs = [document_1, document_2]
from pydantic import BaseModel, Field
class QueryInput(BaseModel):
    query: str =  Field(description="Query to be passed as an argument. Always use this")