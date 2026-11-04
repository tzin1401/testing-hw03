# Bug list — G1 (GitHub Issues)

Nguồn: lượt chạy GUI checklist trên Google Chrome 155. 51 item Failed được gom thành 42 issue theo root cause. Milestone: `HW03 — GUI checklist (Chrome)`.

Thống kê: `is:issue label:"type: bug"` trên https://github.com/tzin1401/testing-hw03/issues

| Issue | Title | Labels |
|---|---|---|
| [#1](https://github.com/tzin1401/testing-hw03/issues/1) | [BUG][login] Login page heading shows "Đăng Ký" instead of "Đăng nhập" | `type: bug` `severity: minor` `priority: P2` `status: new` `module: login` |
| [#2](https://github.com/tzin1401/testing-hw03/issues/2) | [BUG][login] English labels "Username" and "Sign In" on Vietnamese Login form | `type: bug` `severity: minor` `priority: P3` `status: new` `module: login` |
| [#3](https://github.com/tzin1401/testing-hw03/issues/3) | [BUG][login] Login password field displays the password in plain text | `type: bug` `severity: major` `priority: P1` `status: new` `module: login` |
| [#4](https://github.com/tzin1401/testing-hw03/issues/4) | [BUG][ui] Email fields use type="text" so malformed emails are not validated | `type: bug` `severity: minor` `priority: P2` `status: new` `module: ui` |
| [#5](https://github.com/tzin1401/testing-hw03/issues/5) | [BUG][register] Register submit button is red instead of the positive-action blue | `type: bug` `severity: trivial` `priority: P3` `status: new` `module: register` |
| [#6](https://github.com/tzin1401/testing-hw03/issues/6) | [BUG][forgot-password] Reset and Back buttons on step 2 share the same green style | `type: bug` `severity: trivial` `priority: P3` `status: new` `module: forgot-password` |
| [#7](https://github.com/tzin1401/testing-hw03/issues/7) | [BUG][ui] No page has an <h1> heading | `type: bug` `severity: minor` `priority: P3` `status: new` `module: ui` |
| [#8](https://github.com/tzin1401/testing-hw03/issues/8) | [BUG][register] Password rule hint has insufficient contrast (2.54:1) | `type: bug` `severity: minor` `priority: P3` `status: new` `module: register` |
| [#9](https://github.com/tzin1401/testing-hw03/issues/9) | [BUG][login] Sign In button has tabIndex=1 and is focused before the form fields | `type: bug` `severity: minor` `priority: P2` `status: new` `module: login` |
| [#10](https://github.com/tzin1401/testing-hw03/issues/10) | [BUG][profile] Header greeting is not updated after saving a new name | `type: bug` `severity: minor` `priority: P2` `status: new` `module: profile` |
| [#11](https://github.com/tzin1401/testing-hw03/issues/11) | [BUG][navigation] User name is rendered as HTML in the header greeting (stored XSS) | `type: bug` `severity: critical` `priority: P0` `status: new` `module: navigation` |
| [#12](https://github.com/tzin1401/testing-hw03/issues/12) | [BUG][ui] Required fields have no * marker | `type: bug` `severity: trivial` `priority: P3` `status: new` `module: ui` |
| [#13](https://github.com/tzin1401/testing-hw03/issues/13) | [BUG][ui] Form labels are not associated with their inputs | `type: bug` `severity: minor` `priority: P3` `status: new` `module: ui` |
| [#14](https://github.com/tzin1401/testing-hw03/issues/14) | [BUG][register] Register form has no Confirm Password field | `type: bug` `severity: major` `priority: P1` `status: new` `module: register` |
| [#15](https://github.com/tzin1401/testing-hw03/issues/15) | [BUG][register] Password validator requires a space and rejects special characters, contradicting its own message | `type: bug` `severity: critical` `priority: P0` `status: new` `module: register` |
| [#16](https://github.com/tzin1401/testing-hw03/issues/16) | [BUG][register] Duplicate email is accepted, including case/space variants | `type: bug` `severity: critical` `priority: P1` `status: new` `module: register` |
| [#17](https://github.com/tzin1401/testing-hw03/issues/17) | [BUG][login] Login error banner is shown below the submit button | `type: bug` `severity: trivial` `priority: P3` `status: new` `module: login` |
| [#18](https://github.com/tzin1401/testing-hw03/issues/18) | [BUG][forgot-password] Forgot Password has no step indicator | `type: bug` `severity: minor` `priority: P2` `status: new` `module: forgot-password` |
| [#19](https://github.com/tzin1401/testing-hw03/issues/19) | [BUG][forgot-password] OTP has only 4 digits and the OTP input has no length validation | `type: bug` `severity: major` `priority: P1` `status: new` `module: forgot-password` |
| [#20](https://github.com/tzin1401/testing-hw03/issues/20) | [BUG][forgot-password] Reset form has no Confirm New Password field | `type: bug` `severity: major` `priority: P2` `status: new` `module: forgot-password` |
| [#21](https://github.com/tzin1401/testing-hw03/issues/21) | [BUG][ui] Feedback uses blocking alert() instead of inline messages | `type: bug` `severity: minor` `priority: P2` `status: new` `module: ui` |
| [#22](https://github.com/tzin1401/testing-hw03/issues/22) | [BUG][forgot-password] Unknown email reveals "User not found" (account enumeration) | `type: bug` `severity: major` `priority: P2` `status: new` `module: forgot-password` |
| [#23](https://github.com/tzin1401/testing-hw03/issues/23) | [BUG][profile] Valid phone numbers starting with 0 are rejected | `type: bug` `severity: major` `priority: P1` `status: new` `module: profile` |
| [#24](https://github.com/tzin1401/testing-hw03/issues/24) | [BUG][ui] Email/password fields have no autocomplete attributes | `type: bug` `severity: trivial` `priority: P3` `status: new` `module: ui` |
| [#25](https://github.com/tzin1401/testing-hw03/issues/25) | [BUG][forgot-password] New-password rule is not shown on reset step 2 | `type: bug` `severity: minor` `priority: P3` `status: new` `module: forgot-password` |
| [#26](https://github.com/tzin1401/testing-hw03/issues/26) | [BUG][forgot-password] Pasted OTP with surrounding spaces is rejected | `type: bug` `severity: minor` `priority: P2` `status: new` `module: forgot-password` |
| [#27](https://github.com/tzin1401/testing-hw03/issues/27) | [BUG][profile] Long email is cut off in the read-only Profile field | `type: bug` `severity: trivial` `priority: P3` `status: new` `module: profile` |
| [#28](https://github.com/tzin1401/testing-hw03/issues/28) | [BUG][navigation] Navbar does not highlight the current page | `type: bug` `severity: trivial` `priority: P3` `status: new` `module: navigation` |
| [#29](https://github.com/tzin1401/testing-hw03/issues/29) | [BUG][navigation] Cart link has no item-count badge | `type: bug` `severity: minor` `priority: P2` `status: new` `module: navigation` |
| [#30](https://github.com/tzin1401/testing-hw03/issues/30) | [BUG][navigation] Logout button is labelled "Thoát" instead of "Đăng xuất" | `type: bug` `severity: trivial` `priority: P3` `status: new` `module: navigation` |
| [#31](https://github.com/tzin1401/testing-hw03/issues/31) | [BUG][login] "Quên mật khẩu?" link triggers a full page reload | `type: bug` `severity: trivial` `priority: P3` `status: new` `module: login` |
| [#32](https://github.com/tzin1401/testing-hw03/issues/32) | [BUG][forgot-password] Step 1 has no "Quay lại đăng nhập" button | `type: bug` `severity: minor` `priority: P2` `status: new` `module: forgot-password` |
| [#33](https://github.com/tzin1401/testing-hw03/issues/33) | [BUG][forgot-password] Refreshing step 2 loses the reset progress | `type: bug` `severity: minor` `priority: P3` `status: new` `module: forgot-password` |
| [#34](https://github.com/tzin1401/testing-hw03/issues/34) | [BUG][profile] Logged-out /profile shows a dead-end message instead of redirecting | `type: bug` `severity: minor` `priority: P3` `status: new` `module: profile` |
| [#35](https://github.com/tzin1401/testing-hw03/issues/35) | [BUG][navigation] Logged-in users can still open /login and /register | `type: bug` `severity: minor` `priority: P3` `status: new` `module: navigation` |
| [#36](https://github.com/tzin1401/testing-hw03/issues/36) | [BUG][login] Locked account shows the same generic error as a wrong password | `type: bug` `severity: major` `priority: P2` `status: new` `module: login` |
| [#37](https://github.com/tzin1401/testing-hw03/issues/37) | [BUG][login] Old login error stays visible after editing the fields | `type: bug` `severity: trivial` `priority: P3` `status: new` `module: login` |
| [#38](https://github.com/tzin1401/testing-hw03/issues/38) | [BUG][register] No success message after a successful registration | `type: bug` `severity: minor` `priority: P3` `status: new` `module: register` |
| [#39](https://github.com/tzin1401/testing-hw03/issues/39) | [BUG][profile] Empty order history has no icon/illustration | `type: bug` `severity: trivial` `priority: P3` `status: new` `module: profile` |
| [#40](https://github.com/tzin1401/testing-hw03/issues/40) | [BUG][ui] Submit buttons have no loading state and allow duplicate requests | `type: bug` `severity: major` `priority: P2` `status: new` `module: ui` |
| [#41](https://github.com/tzin1401/testing-hw03/issues/41) | [BUG][ui] Feedback messages are not exposed to assistive technology | `type: bug` `severity: minor` `priority: P3` `status: new` `module: ui` |
| [#42](https://github.com/tzin1401/testing-hw03/issues/42) | [BUG][ui] Server failure messages are inconsistent and raw | `type: bug` `severity: minor` `priority: P3` `status: new` `module: ui` |
