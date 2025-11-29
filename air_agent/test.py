import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from air_agent.agent import root_agent

print("Agent type:", type(root_agent))
print("Attributes:")
print(dir(root_agent))
