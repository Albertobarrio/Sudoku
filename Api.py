
import requests

#TODO: Conectar api con Interface y hacer lost est de la api

class Api():
    
    def positions_fixed(self):
        positionfixed={}
        resp = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=9')
        JSON = resp.json()['squares']
        for i in range(len(JSON)):
            positionfixed.setdefault((JSON[i]['x']*9)+JSON[i]['y'],JSON[i]['value'])
        return positionfixed
    
    def make_board(self):
        board=""
        positionfixed = self.positions_fixed()
        for i in range(81):
            if i in positionfixed:
                board += str(positionfixed[i])
            else:
                board += "x"
        return board   

api= Api()
print(api.make_board())