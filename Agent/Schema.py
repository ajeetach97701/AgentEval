from pydantic import BaseModel, Field
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

docs = [Document(metadata={}, page_content='#Question :What are the MEMBERSHIP PLANS AND THEIR PRICE DETAILS ? Answer in english:\nThe membership/subsctiption details are as follows:\n1. Auto-renewable monthly subscription: priced at 235 SAR, with a registration fee of 50 SAR. Additional joining fees will be removed when it is renewed. Please note that this membership has auto-renew, but you can still use it for 1 month by cancelling the auto renewal. \n2. Two-month subscription (+ 1 free month): priced at 450 SAR\n3. Six-month subscription: priced at 1,230 SAR\n4. Twelve-month subscription: priced at 1,960 SAR\n5. 50 SAR registration fee is applied in all subscription type. Answer in Arabic:\nاشتراك شهري متجدد تلقائيًا: بسعر 235 ريال سعودي، مع رسوم تسجيل 50 ريال سعودي.\nاشتراك لمدة شهرين (+ شهر مجاني): بسعر 450 ريال سعودي، مع رسوم تسجيل 50 ريال سعودي.\nاشتراك لمدة 6 أشهر: بسعر 1230 ريال سعودي، مع رسوم تسجيل 50 ريال سعودي.\nاشتراك لمدة 12 شهرًا: بسعر 1960 ريال سعودي، مع رسوم تسجيل 50 ريال سعودي.'),
 Document(metadata={}, page_content='#Question in English: HOW DOES MONTHLY MEMBERSHIP WORK? Question in Arabic: ماهي آلية عمل الإشتراك الشهري ؟ Answer in English : When you join, you will be charged for the first month along with a joining fee, which is subject to change. The payment card details you provide at the time of joining will be used for automatic monthly payments to maintain your ongoing subscription. It is important to ensure there are sufficient funds in your account on the scheduled payment date to cover the monthly membership fee. You can cancel your membership renewal through your account, but please note that this must be done at least 5 days before the expiration date. If a payment fails, your membership will be canceled, and you will no longer have access to the gym. To ensure a smooth experience at Activ Gym, please choose the correct payment card and make sure it is funded before the recurring payment date. Answer in Arabic : عند الانضمام الى أكتيف جيم ، سيتم تحصيل رسوم الشهر الأول منك ورسوم الانضمام (  بناء على العرض المتوفر )\nسيتم استخدام تفاصيل بطاقة الدفع التي ستسجلها عند انضمامك إلينا للدفع مقابل اشتراكك المستمر بطريقة شهرية. سنقوم بتحصيل مدفوعاتك الشهرية تلقائيًا بطريقة أوتوماتيكية، بحيث يمكنك الاستمرار في استخدام خدمات وصالات أكتيف جيم  بدون انقطاع للمدة التي تريدها\nتأكد من توفر قيمة التجديد في يوم التجديد لتغطية قيمة اشتراكك الشهري في أكتيف جيم\nبإمكانك ايضاف إلغاء التجديد التلقائي لاشتراكك من خلال الدخول على حسابك في الموقع الإلكتروني . (يجب التأكد من من الالغاء قبل 5 ايام من تاريخ نهاية الاشتراك) .\n في حال فشل الدفع عند التجديد التلقائي , سيتم ايقاف اشتراكك ولن يكون باستطاعتك الدخول إلى النادي وزيارتنا\nلتجنب حدوث ذلك والاستمتاع بتجربتك في أكتيف جيم , تأكد من وجود قيمة الاشتراك في بطاقتك قبل يوم التجديد التلقائي'),
 Document(metadata={}, page_content="#Question : How can I join? Answer in English : Joining is simple! Just be sure you're over 18, fill in your details, choose the plan that suits you, and complete payment. Your membership will be activated immediately after you join. Answer in Arabic : يمكنك الانضمام إلى نادي أكتيف من خلال زيارة موقعنا الإلكتروني أو التطبيق الخاص بنا للتسجيل. يمكنك أيضًا زيارة النادي شخصيًا للتسجيل والحصول على مزيد من المعلومات حول الاشتراكات المتاحة. هل ترغبين في ترتيب زيارة لتجربة النادي قبل الانضمام؟"),
 Document(metadata={}, page_content='#Question: What are terms and condition regarding fees and charges? Part 1:\nAll published membership fees or other charges inclusive of all types of taxes such as The tax registration number for ACTIV gyms is 3000096456620001 and this applies to all fees from ACTIV gyms applicable under these terms and conditions. The VAT is included in your invoice.\n \n\n"Payment" means the membership term subscription fee for ACTIV according to the option of purchased membership which is determined by the duration of the subscription when joining. Our memberships are in terms of 1, 3, 6 & 12 months and some of them are automatically renewed at the end of each term. In such a case, your card details will be saved securely for such automatic recurring payments. Payments are charged in full at the beginning of each term, upfront, and apart from cancellations in accordance with the terms. No partial fees will be refunded from the subscription fee unless you cancel within 24 hours of your membership commencement date in your first term, in accordance with the Ministry of Sports Consumer Protection guidelines for Sports and Gymnasiums. Monthly "Frequent payment" or "recurring payment" means the membership monthly fees as per the selected price option will be deducted monthly as agreed by clicking purchase this will continue until such time that this is canceled. If your monthly membership has been renewed, you can\'t ask to a refund it or cancel it under any circumstances. A "joining fee" will be charged upon becoming a member. The joining fee is a one-time non-refundable payment when you sign up and is applied to cover the initial management costs associated with setting up a new subscription and allowing you to receive two free introductory sessions with a trainer. During certain periods of special offers, for example, pre-opening, ACTIV management may choose, at its own discretion, to cancel or reduce joining fees. The recurring  membership will automatically renew on the membership expiry date. You cannot modify the renewal payment date, but we reserve the right to modify the payment date at our own discretion.'),
 Document(metadata={}, page_content='#Question in English : WHAT MEMBERSHIP OPTIONS ARE AVAILABLE? Question in Arabic: ماهي انواع الاشتراكات المتوفرة ؟ Answer in English : We offer 2 types of memberships :\n1- Recurring with no commitment  available on monthly membership.\n2- Upfront payment with commitment available for 3 ,6 12 months. Answer in Arabic : نقدم في أكتيف جيم خيارات متنوعة من  الاشتراكات\n1- اشتراك  تلقائي التجديد  وبدن التزام  وحاليا يتوفر على باقة الشهرية\n2- اشتراك مقدم بالتزام لفترة زمنية ويتوفر على باقات ال3 و6 و12 شهر')]

class QueryInput(BaseModel):
    query: str = Field(
        description="Query to be passed as an argument. Always use this")
