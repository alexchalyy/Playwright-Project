'''

This is Python Playwright personal portfolio test script.

This script adds an item to a to do list on a test web site, verifies it can be moved from active to completed state, and then deletes it.

Written by Alex Chalyy on 10/15/2026.

'''

import re
from playwright.sync_api import Page, expect

#---------------------------------------------------------------------------------
def test_start(page: Page):

    page.goto("https://demo.playwright.dev/todomvc") # open playwright test page

    expect(page.get_by_text("todos")).to_be_visible() # verifies page has "todos" text

    page.get_by_role("textbox").fill("Get milk") # fill in the textbox with "Get Milk" and press Enter
    
    page.keyboard.press("Enter")
    
    expect(page.get_by_text("Get milk")).to_be_visible() # verifies "Get milk" is visible on the page
    
    page.get_by_text("Active").click() # This command clicks on the "Active" filter to show only active items.
    
    expect(page.get_by_text("Get milk")).to_be_visible() # verifies "Get Milk" is visible on the page
    
    page.get_by_text("Completed").click() # This command clicks on the "Completed" filter to show only completed items.
    
    page.get_by_text("Get milk").is_hidden() # verifies "Get Milk" is hidden on the page

    # This command clicks on the "All" filter to show only all items.
    page.locator("xpath=/html/body/section/div/footer/ul/li[1]/a").click()

    page.get_by_role("checkbox", name="Toggle Todo").check()

    expect(page.get_by_text("Get milk")).to_be_visible() # verifies "Get Milk" is visible on the page

    page.get_by_text("Active").click() # This command clicks on the "Active" filter to show only active items.
    
    expect(page.get_by_text("Get milk")).to_be_hidden() # verifies "Get Milk" is hidden on the page

    # This command clicks on the "Completed" filter to show only completed items.
    
    page.locator("xpath=/html/body/section/div/footer/ul/li[3]/a").click()

    expect(page.get_by_text("Get milk")).to_be_visible() # verifies "Get milk" is visible on the page

    page.locator("xpath=/html/body/section/div/section/ul/li/div/button").click() # This command clicks on the "Delete" button to delete the item.

    expect(page.get_by_text("Get milk")).to_be_hidden() # verifies "Get Milk" is hidden on the page
