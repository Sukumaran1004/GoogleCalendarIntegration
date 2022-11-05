# GoogleCalendarIntegration

Implement google calendar integration using django rest api. 
You need to use the OAuth2 mechanism to get users calendar access. 
Below are detail of API endpoint and corresponding views which you need to implement 
1./rest/v1/calendar/init/ -> GoogleCalendarInitView() This view should start 
step 1 of the OAuth. Which will prompt user for his/her credentials 
2. /rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()
