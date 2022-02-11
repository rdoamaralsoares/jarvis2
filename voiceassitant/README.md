# CODE STRUCTURE

## WelcomeRecepcionist
Chatbot Responsible for interacting with the conversation, it has the artificial intelligence modules and makes the calls to all the APIs necessary to build a fluid flow of the conversation. 

## msflow_opendoor
Microsoft Flow that receives the request via HTTP call and opens the port through an internal server.

## msflow_wifi
Microsoft Flow that receives the request via HTTP call and interacts with the internal Cisco ISE API to create the guest account.

## msflow_adviseinteams
Microsoft Flow that identifies the address of the internal contributor through Microsoft Graph and then makes a call to the bot created in Webex to notify him.

## CiscoISE.swagger.json
Microsoft Flow custom connector, required to be able to communicate with the internal API and interactions with Cisco ISE.

## duo_api_nodejs
Azure Function responsible for forwarding requests to Cisco DUO
