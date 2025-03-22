# Testing

This document describes the test cases for the Shopping List application.

## Test Cases

### TC001: Add a New Item

*   **Description:** Verify that a new item can be added to the shopping list and persisted in the database.
*   **Preconditions:** The application must be running with Gunicorn. The database must be initialized, or should be created automatically if it doesn't.
*   **Steps:**
    1.  Open the application in a web browser at `http://localhost:5000`.
    2.  Enter an item name in the input field.
    3.  Click the "Add" button.
*   **Expected Results:**
    *   The item should be added to the shopping list and displayed correctly on the page.
    *   There should not be any exceptions.
    *   The code should check every function to ensure code is running as expected.
*   **Actual Results:** The item was added to the shopping list and displayed correctly, no database or code problems found.
*   **Status:** Pass
*   **Date:** 2025-03-22
*   **Author:** Conjuror09

### TC002: Add Multiple Items

*   **Description:** Verify that multiple items can be added to the shopping list and all persisted to the database.
*   **Preconditions:** The application must be running with Gunicorn. The database must be initialized, or should be created automatically if it doesn't.
*   **Steps:**
    1.  Open the application in a web browser at `http://localhost:5000`.
    2.  Add several items to the shopping list, entering each item and then clicking the "Add" button.
*   **Expected Results:** All items should be displayed correctly in the shopping list.
*   **Actual Results:** All items were displayed correctly in the shopping list and to the database.
*   **Status:** Pass
*   **Date:** 2025-03-22
*   **Author:** Conjuror09

### TC003: Refresh the Page

*   **Description:** Verify that the shopping list items are persisted in the database and reloaded correctly after refreshing the page.
*   **Preconditions:** The application must be running with Gunicorn. The database must be initialized. The shopping list must contain at least one item.
*   **Steps:**
    1.  Open the application in a web browser at `http://localhost:5000`.
    2.  Add an item to the shopping list.
    3.  Refresh the page in the browser.
*   **Expected Results:** The item should still be displayed in the shopping list after the page is refreshed.
*   **Actual Results:** The item was still displayed in the shopping list after the page was refreshed.
*   **Status:** Pass
*   **Date:** 2025-03-22
*   **Author:** Conjuror09

### TC004: style.css was connected

*   **Description:** Verify that the CSS file is being connected to the front end and that the changes can be seen
*   **Preconditions:** The application must be running with Gunicorn. The linked style must affect the app and to see if caching errors
*   **Steps:**
    1.  Set the body to background-color: lightblue
    2.  Hard refresh the page on the browser
*   **Expected Results:** The whole page will be on light blue.
*   **Actual Results:** The whole page was light blue and the network activity confirms it to be true.
*   **Status:** Pass
*   **Date:** 2025-03-22
*   **Author:** Conjuror09

### TC005: Authentication with SSH keys

*   **Description:** Verify that the authencation with SSH keys and that you can add and send all the files to a remote server.
*   **Preconditions:** Create SSH Key with a trusted source, and that authentication to Github has already been tested.
*   **Steps:**
    1.  Write code to see it work.
    2.  Check `git status` to show that all files will be sent.
    3.  Commit to changes
    4.  Push to remote.
*   **Expected Results:** The results on the remote matches what you have.
*   **Actual Results:** As said on previous results, it will push without the need for login information.
*   **Status:** Pass
*   **Date:** 2025-03-22
*   **Author:** Conjuror09

