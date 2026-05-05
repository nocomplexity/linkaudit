# Security Policy


## Reporting a Vulnerability

Send an email or submit an github issue if you see a vulnerability that **SHOULD** be addressed.

## Security Information

I advocate for better and [simple security](simplifysecurity.nocomplexity.com), so this tool is reviewed to identify potential vulnerabilities.

URL processing **Should** always be done carefully, since using `urlopen` can lead to parsing errors.
Checking the status of an URL requires using a construct like:
```python
request = Request(url, headers=nocxheaders)
	            with urlopen(request, timeout=nocxtimeout) as response:
	                return url, response.status
```

Mitigation to our judgement:
* Content of URLs is not processed.
* Only the DNS or HTTP status of an URL is verified.
* Use of more vulnerable external libraries, like `requests` or `aiohttp` are deliberately avoided.


