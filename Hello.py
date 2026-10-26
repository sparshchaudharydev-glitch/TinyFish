import os
from dotenv import load_dotenv
from tinyfish import TinyFish

load_dotenv()

os.environ["TINYFISH_RUNTIME_ATTEMPT_ID"] = "99a66dae-50ff-4867-806a-01aa01585f6c"

api_key = TinyFish()

response = api_key.search.query(
    "latest FIFA World Cup news today",
    location="US",
    language="en",
)

for result in response.results:
    print(result.title, result.url)