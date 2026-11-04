# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: run-firefox.spec.js >> IA-03-03 The navigation item for the current screen is visually highlighted.
- Location: checklist/automation/run-firefox-shared.cjs:24:2

# Error details

```
Error: /login: active={"href":"/login","color":"rgb(255, 255, 255)","bg":"rgba(0, 0, 0, 0)","decoration":"none","fontWeight":"400","aria":null}; inactive={"href":"/login","color":"rgb(255, 255, 255)","bg":"rgba(0, 0, 0, 0)","decoration":"none","fontWeight":"400","aria":null}
/register: active={"href":"/register","color":"rgb(255, 255, 255)","bg":"rgba(0, 0, 0, 0)","decoration":"none","fontWeight":"400","aria":null}; inactive={"href":"/register","color":"rgb(255, 255, 255)","bg":"rgba(0, 0, 0, 0)","decoration":"none","fontWeight":"400","aria":null}
Profile active color=rgb(253, 224, 71), bg=rgba(0, 0, 0, 0); Home same link color=rgb(253, 224, 71), bg=rgba(0, 0, 0, 0)

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```