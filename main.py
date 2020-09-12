from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium
import pathlib
import SudokuSolver

chromeDriver = str(pathlib.Path().absolute()) + "\\venv\\chromedriver-Windows"
driver = webdriver.Chrome(chromeDriver)
driver.get("https://www.nytimes.com/puzzles/sudoku/hard")

gameBoard = []
for i in range(9):
    gameBoard.append([])

content = driver.find_element_by_class_name('su-board')
suList = content.find_elements_by_class_name("su-cell")
row = 0
col = 0
for element in suList:
    numAttribute = element.get_attribute("aria-label")
    if numAttribute != "empty":
        gameBoard[row].append([True, int(numAttribute)])
    else:
        gameBoard[row].append([False, 0])
    col += 1
    if col == 9:
        row += 1
        col = 0
print("Game Board: ")
for i in range(9):
    for j in range(9):
        print(gameBoard[i][j][1], end = " ")
    print()

solver = SudokuSolver.SudokuSolver(gameBoard)
gameBoard = solver.run()

action = ActionChains(driver)

if gameBoard != None:
    for element in suList:
        index = int(element.get_attribute("data-cell"))
        col = index % 9
        row = int(index / 9)
        if not gameBoard[row][col][0]:
            action.send_keys_to_element(element, gameBoard[row][col][1])
    action.perform()

input("Type anything to quit: ")
driver.quit()
