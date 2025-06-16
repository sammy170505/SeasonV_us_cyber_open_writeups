┌──(env)─(kali㉿kali)-[~/Downloads/us_open_ctf/Crypto]
└─$ echo "QWZ0ZXIgaW5zcGVjdGluZyB0aGUgY29udGVudHMsIGhlJ2xsIGhvcCBvbiB0aGUgUk9CT1QgdmFjY3V1bSBwaWNraW5nIHVwIHRoZSBjcnVtYnMgaGUgbWFkZS4KQ3J1bWIgMTogZFY5Q1FHc3paRjloVA==" | base64 -d 

After inspecting the contents, he'll hop on the ROBOT vaccuum picking up the crumbs he made.
Crumb 1: dV9CQGszZF9hT   

Got to: https://fydqlgcm.web.ctf.uscybergames.com/robots.txt

result:

User-agent: *
Disallow: /admin

# The robot vaccuum arrives at a locked door, which naturally he'll want to get inside
# Crumb 2: jB0SDNSX2MwMG

go to  https://fydqlgcm.web.ctf.uscybergames.com/admin

look for static javascript:
const ADMIN_USER = 'admin';
const CRUMB_3 = 'sxM19mT3JfZEF';
