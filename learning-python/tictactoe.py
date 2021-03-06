#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import random


class TicTacToe(wx.Frame):
    board = {}
    scale = {'width': 90, 'height': 90}
    moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, parent, title):

        super(TicTacToe, self).__init__(parent, title=title,
                                        size=(400, 400))
        self.Centre()
        self.Show()
        self.playgame()

    def drawboard(self):
        dc = wx.ClientDC(self)
        column = 10
        row = 15
        z = 0
        for x in range(0, 3):
            for y in range(0, 3):
                self.board[z] = column, row, self.scale['width'],\
                    self.scale['height']
                dc.DrawRectangle(column, row, int(self.scale['width']),
                    int(self.scale['height']))
                dc.DrawLabel(str(z), self.board[z], wx.LC_ALIGN_TOP)
                column = column + 100
                z = z + 1
            column = 10
            row = row + 100
        forecolor = (153, 0, 0)
        dc.SetTextForeground(forecolor)
        self.Update()

    def updateboard(self, boardpos=-1, player=""):
        dc = wx.ClientDC(self)
        dc.DrawLabel(player, self.board[boardpos], wx.ALIGN_CENTER)
        self.Update()

    def dlgquestion(self, parent=None, message='', default_value='Test'):
        dlg = wx.TextEntryDialog(parent, message, style=wx.OK, pos=wx.Point(0, 0))
        dlg.ShowModal()
        result = dlg.GetValue()
        dlg.Destroy()
        return result

    def updatemoves(self, pos, player):
        self.moves[pos] = player
        self.Update()
        self.updateboard(int(pos), "P1")

    def findmoves(self):
        cpumoves = []
        for x in xrange(9):
            if self.moves[x] == int(x):
                cpumoves.insert(x,x)
        if len(cpumoves) == 0:
            return -1;
        return cpumoves

    def computermoves(self, player):
        choice = random.choice(self.findmoves())
        print choice
        if choice == -1:
            print "Sorry, no more moves!"
            return -1
        else:
            self.moves[choice] = player
            self.Update()
            self.updateboard(int(choice), "C")
            return 0

    def checkmoves(self, le):
        return ((self.moves[0] == le and self.moves[1] == le and self.moves[2] == le) or  # across the top
                (self.moves[3] == le and self.moves[4] == le and self.moves[5] == le) or  # across the middle
                (self.moves[6] == le and self.moves[7] == le and self.moves[8] == le) or  # across the bottom
                (self.moves[0] == le and self.moves[3] == le and self.moves[6] == le) or  # down the left side
                (self.moves[1] == le and self.moves[4] == le and self.moves[7] == le) or  # down the middle
                (self.moves[2] == le and self.moves[5] == le and self.moves[8] == le) or  # down the right side
                (self.moves[2] == le and self.moves[4] == le and self.moves[6] == le) or  # diagonal
                (self.moves[0] == le and self.moves[4] == le and self.moves[8] == le))  # diagonal

    def playgame(self):
        self.drawboard()
        answer = self.dlgquestion(message="Enter \"Y\" to go first or enter to skip")
        if (answer) != "Y":
            self.computermoves("C")

        while True:
            pos = self.dlgquestion(message='Please select a move')
            if pos == "Q":
                quit()
            self.updatemoves(int(pos), "P1")
            if self.checkmoves("P1"):
                print ("P1 is the Winner!")
                break;
            if (self.computermoves("C") == -1):
                break;
            if self.checkmoves("C"):
                print ("Computer is the Winner!")
                break;


if __name__ == '__main__':
    app = wx.App()
    TicTacToe(None, 'Line')
    app.MainLoop()
