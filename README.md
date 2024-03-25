
# MailTMClient
I would like to bring to your attention the user-friendly MailTMClient package, specifically designed to facilitate seamless communication with the mail.tm API. With its comprehensive set of functions, it emerges as the only Python-based solution out there that fully embraces all the API's offerings.
My mail.tm console client is based on the MailTMClient and in the [source code of its main.py](https://github.com/RPwnage/binify/blob/main/main.py) file you can see the ease of use of MailTMclient from an example.

## Registering a new Account and logging in

Using the code below, a new account can be created. 

    from MailTMClient import MailTMClient
    (responseCode, response) = MailTMClient().register(args.address, args.password)
        if responseCode == 0:
            print("[i] Successfully created an MailTM Account!")
            saveTokenToFile(response)
        if responseCode != 0:
            print("[!] Failed to create an MailTM Account! (" + str(response) + ")")

Following a successful account creation, the response variable will contain the tokens required for future application access. In order to log in to an existing account, please proceed accordingly.

    (responseCode, response) =  MailTMClient().login(args.address, args.password)

