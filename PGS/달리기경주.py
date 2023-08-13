def solution(players, callings):
  player_dict = {}
  for i in range(len(players)):
    player_dict[players[i]] = i
      
  for calling in callings:
    rank = player_dict[calling]
    player_dict[calling] -= 1
    player_dict[players[rank - 1]] += 1
    
    players[rank], players[rank - 1] = players[rank - 1], players[rank]
      
  return players