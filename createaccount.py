import mechanize
import cookielib
import subprocess

br = mechanize.Browser()

#cookies
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

#browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

#user agent
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
#username and pw
username_prefix = 'winner2014'
pw = 'pw12345pw'
range

def createAccount(i):
    username = username_prefix+str(i)
    r = br.open('http://mobile.twitter.com/signup')
    br.form = list(br.forms())[0]
    #name
    control = br.form.find_control('oauth_signup_client[fullname]')
    control.value = username
    #email
    control = br.form.find_control('oauth_signup_client[phone_number]')
    control.value = username+'@yopmail.com'     #any email provider here works as the competition does not require accounts to be verified
    #password
    control = br.form.find_control('oauth_signup_client[password]')
    control.value = pw
    #submit
    r=br.submit()
    #handle matching existing usernames
    username = list(br.forms())[0]   #pick first username suggested
    br.form = username
    #submit
    r=br.submit()
    #Finish account
    link = list(br.links())[2]
    request = br.click_link(link)
    response = br.follow_link(link)
    #go to account
    link = list(br.links())[5]
    request = br.click_link(link)
    response = br.follow_link(link)
    #logout
    br.form = list(br.forms())[3]
    r=br.submit()


    print("Twitter account "+username+" created")

    return username

i = int(raw_input("start in which number? (ie. winner2014xxx)\n"))
j = int(raw_input("end in which number? (ie. winner2014xxx)\n"))
for i in xrange (i,j):
    username = createAccount(i)
    
    #Call the casperjs voting script here, passing the username and password
