# linkExtractor
 This script goes to a website and grabs the anchor tag href and name. It filters to remove links that do not begin with the library proxy prefix. It writes the name (or None, if not available) and URL to a file. # I wrote this to quickly grab database names and URLs from the library website for link testing purposes (finding links that were redirecting, etc.)
 
 Requires urlib, BeautifulSoup, ssl
