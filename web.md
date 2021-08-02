# Web

# Refs

* [HTTP Status Codes](http://racksburg.com/choosing-an-http-status-code/)

# URL Unreserved Characters and Percent Encoding

Quoting from the [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2.3):

```
pchar         = unreserved / pct-encoded / sub-delims / ":" / "@"
unreserved    = ALPHA / DIGIT / "-" / "." / "_" / "~"
pct-encoded   = "%" HEXDIG HEXDIG
sub-delims    = "!" / "$" / "&" / "'" / "(" / ")"
              / "*" / "+" / "," / ";" / "="
```
