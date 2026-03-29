from fastapi import APIRouter
from products.model import Product
from products.repository import ProductRepository
from products.service import ProductService
from core.database import get_engine


products_api = APIRouter(prefix="/products", tags=["products"])

repo = ProductRepository(get_engine())
service = ProductService(repo)


@products_api.get("/")
async def get_products() -> list[Product]:
    return service.get_products()
    # load_dotenv()

    # DATABASE_URL = os.getenv("DATABASE_URL")
    # engine = create_engine(DATABASE_URL)

    # with engine.connect() as conn:
    #     result = conn.execute(
    #         text("SELECT id, name FROM dbo.products WHERE price > :price"), {"price": 2}
    #     )
    #     for row in result:
    #         print(row)

    # products = [
    #     Product(
    #         id=1,
    #         name="Wireless Mouse",
    #         price=22.99,
    #         description="The Wireless Mouse is designed for comfort and efficiency, offering a sleek and ergonomic design that fits perfectly in your hand. Ideal for both everyday use and professional environments, this mouse provides the freedom of wireless connectivity with the reliability of a wired device.",
    #         # features=[
    #         #     "Ergonomic Design: The contoured shape and soft rubber grips ensure that your hand remains comfortable, even after long hours of use.",
    #         #     "Wireless Connectivity: Enjoy the convenience of wireless technology with a reliable connection up to 10 meters (33 feet) away.",
    #         #     "High Precision: With a 1600 DPI optical sensor, this mouse delivers smooth and accurate tracking on almost any surface.",
    #         #     "Long Battery Life: The mouse uses a single AA battery (included) and can last up to 12 months before needing a replacement.",
    #         #     "Plug-and-Play: Simply plug the USB receiver into your computer’s USB port and start using your mouse right away, without the need for additional software.",
    #         #     "Portable Size: Lightweight and compact, it’s easy to take this mouse with you wherever you go.",
    #         # ],
    #     ),
    #     Product(
    #         id=2,
    #         name="Mechanical Keyboard",
    #         price=79.99,
    #         description="A high-quality mechanical keyboard with customizable RGB lighting, offering a tactile and responsive typing experience for both gaming and professional use.",
    #         features=[
    #             "Customizable RGB Lighting: Personalize your keyboard with millions of colors and various lighting effects.",
    #             "Tactile Switches: Enjoy the satisfying click and tactile feedback with each keystroke.",
    #             "Durable Build: Constructed with a sturdy aluminum frame for long-lasting durability.",
    #             "Full Key Rollover: Ensures every keypress is registered, even during intense gaming sessions.",
    #             "Programmable Macros: Customize and record macros for complex commands.",
    #             "Ergonomic Design: Comes with a detachable wrist rest for added comfort.",
    #         ],
    #     ),
    #     Product(
    #         id=3,
    #         name="Gaming Headset",
    #         price=59.99,
    #         description="A surround sound gaming headset with a noise-canceling microphone, designed for immersive audio and clear communication.",
    #         # features=[
    #         #     "Surround Sound: Experience immersive 7.1 virtual surround sound.",
    #         #     "Noise-Canceling Microphone: Communicate clearly with a noise-canceling boom mic.",
    #         #     "Comfortable Design: Soft memory foam ear cushions and an adjustable headband for long gaming sessions.",
    #         #     "In-line Controls: Easily adjust volume and mute the microphone with in-line controls.",
    #         #     "Durable Build: Made with high-quality materials for durability.",
    #         #     "Cross-Platform Compatibility: Works with PC, consoles, and mobile devices.",
    #         # ],
    #     ),
    # ]
    # return products
