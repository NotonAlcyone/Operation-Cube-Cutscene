from Main import *

root.title("Someone's Fragment")

characterOne = canvasCenterX - 150
characterTwo = canvasCenterX + 150
characterYCenter = canvasCenterY  + 150

"""
scene = Scene("", "", '')
scenes.append(scene)

#scene.addCharacter("",  , )
"""
scene = Scene("AR-15_background.png", "", '............AR-15 가 실종된지 5일 후.')
scenes.append(scene)

scene = Scene("AR-15_background.png", "헬리안", '......크루거 님, 이상이 AR-15와 관련된 최신정보입니다. 지휘관과 AR팀은 아직 수색에 열중하고 있습니다.')
scenes.append(scene)

scene = Scene("AR-15_background.png", "헬리안", '추가로, 방금 404소대가 신청한 【긴급지휘권】 건에 대해서, 제가 방금 권한을 승인했습니다. ')
scenes.append(scene)

scene = Scene("AR-15_background.png", "크루거", '......어쩔 수 없는 상황이 아니라면 권한을 주지 말았어야 했을 텐데. ')
scenes.append(scene)

scene = Scene("AR-15_background.png", "헬리안", '404 소대가 상대하고 있는 위협이 예상보다 심각합니다.')
scenes.append(scene)

scene = Scene("AR-15_background.png", "헬리안", '어쩌면 그 재머가 정말로 【우산】 계획과 관련이 있을 수도 있습니다.')
scenes.append(scene)

scene = Scene("AR-15_background.png", "크루거", '음......')
scenes.append(scene)

scene = Scene("AR-15_background.png", "크루거", '404 소대는 지금 어디에 있지? ')
scenes.append(scene)

scene = Scene("black.png","헬리안", '아직 S06구역에 있습니다. 벌써 작전을 시작했다고 합니다.')
scenes.append(scene)

scene = Scene("black.png","헬리안", '더 자세한 정보는, 그녀들이 살아서 가져오기를 기대하도록 하죠. ')
scenes.append(scene)

scene = Scene("black.png","", '......같은 시각, S06구역, 철혈 분쟁지대. ')
scenes.append(scene)

scene = Scene("black.png", "UMP9", '야. 일어나.')
scenes.append(scene)

scene = Scene("black.png", "UMP9", '416, 빨리 일어나라고~!')
scenes.append(scene)

scene = Scene("black.png", "UMP9", '야~~~~! ')
scenes.append(scene)

scene = Scene("black.png", "HK416", '윽......')
scenes.append(scene)

scene = Scene("black.png", "HK416", '......시끄러워.')
scenes.append(scene)

scene = Scene("street_dark.png", "UMP9", '헤이! 아직 괜찮아? 416? ')
scene.addCharacter("UMP9_2.png", canvasCenterX  ,characterYCenter )
scenes.append(scene)

scene = Scene("street_dark.png", "HK416", '만약 내가 "멋진걸" 이라고 말하는 게 듣고 싶다면, 빨리 저 돌 좀 치우기나 해 줘.')
scene.addCharacter("UMP9_2.png", canvasCenterX  ,characterYCenter )
scenes.append(scene)

scene = Scene("street_dark.png", "UMP9", '좋아, 철혈의 척살대가 오기까지 아직 3분이나 남았으니, 그동안 뭐라도 해볼게.')
scene.addCharacter("UMP9_2.png", canvasCenterX  ,characterYCenter)
scenes.append(scene)

scene = Scene("street_dark.png", "UMP9", '(돌을 옮기며) 포격소리 들었어? 상황이 안좋아지면 난 내뺄 거다?')
scene.addCharacter("UMP9.png", canvasCenterX  ,characterYCenter )
scenes.append(scene)

scene = Scene("street_dark.png", "HK416", '내빼기만 해봐, 내가 니 머리통을 비틀어서 데리고 올테니까...그것도 머리통만!')
scene.addCharacter("UMP9_1_dark.png",characterTwo  ,characterYCenter)
scene.addCharacter("HK416_1.png", characterOne ,characterYCenter  )
scenes.append(scene)

scene = Scene("street_dark.png", "UMP9", '화내지 말라고, 내 잘못도 아닌걸, 철혈이 들이닥칠줄 누가 알았겠어. ')
scene.addCharacter("HK416_1_dark.png",characterOne  ,characterYCenter )
scene.addCharacter("UMP9_2.png", characterTwo,characterYCenter  )
scenes.append(scene)

scene = Scene("street_dark.png", "UMP9", '그나저나 통신 재머일 뿐인데, 쟤들이 왜 저렇게 목숨을 거는지 모르겠단 말이야.')
scene.addCharacter("HK416_1_dark.png",characterOne  ,characterYCenter )
scene.addCharacter("UMP9.png", characterTwo,characterYCenter  )
scenes.append(scene)

scene = Scene("street_dark.png", "HK416", '우리가 너무 간단하게 생각했어. 헬리안이 보수를 그렇게 높게 부르다니, 애초부터 문제가 있었던 거야. ')
scene.addCharacter("UMP9_1_dark.png",characterTwo  ,characterYCenter)
scene.addCharacter("HK416_1.png", characterOne ,characterYCenter  )
scenes.append(scene)

scene = Scene("street_dark.png", "UMP9", '그러니까 말이야. 사방에 레이더가 깔려 있어서 살짝만 노출해도 공격 당한다고.')
scene.addCharacter("HK416_1_dark.png",characterOne  ,characterYCenter )
scene.addCharacter("UMP9_4.png", characterTwo,characterYCenter  )
scenes.append(scene)

scene = Scene("street_dark.png", "HK416", '야간 작전을 하게 되었으니, 최대한 빨리 그 레이더들을 점령해야 돼. 이러다간 시야도 확보 하지 못할 판이야.')
scene.addCharacter("UMP9_4_dark.png",characterTwo  ,characterYCenter)
scene.addCharacter("HK416_1.png", characterOne ,characterYCenter  )
scenes.append(scene)

scene = Scene("street_dark.png", "UMP9", '우리 둘만 가지고는 안된다고, 이번 척살대에는 장갑부대까지 껴있는 걸.')
scene.addCharacter("HK416_1_dark.png",characterOne  ,characterYCenter )
scene.addCharacter("UMP9.png", characterTwo,characterYCenter  )
scenes.append(scene)

scene = Scene("street_dark.png", "HK416", '그래?....')
scene.addCharacter("UMP9_1_dark.png", characterTwo,characterYCenter  )
scene.addCharacter("HK416_1.png", characterOne ,characterYCenter  )
scenes.append(scene)

scene = Scene("street_dark.png", "HK416", '어쩐지 총알이 안먹히더라. 철갑탄 좀 구해볼 수 있겠어?')
scene.addCharacter("UMP9_1_dark.png", characterTwo,characterYCenter  )
scene.addCharacter("HK416_1.png", characterOne ,characterYCenter  )
scenes.append(scene)

scene = Scene("street_dark.png", "UMP9", '45 언니가 아직 생각 중이긴 한데, 잘 모르겠어. 단서가 있기나 할지...')
scene.addCharacter("HK416_1_dark.png",characterOne  ,characterYCenter )
scene.addCharacter("UMP9.png", characterTwo,characterYCenter  )
scenes.append(scene)

scene = Scene("street_dark.png", "HK416", '：거짓말 치지마, 9. 45가 이미 다 준비해 놨지?')
scene.addCharacter("UMP9_1_dark.png", characterTwo,characterYCenter  )
scene.addCharacter("HK416_1.png", characterOne ,characterYCenter  )
scenes.append(scene)

scene = Scene("street_dark.png", "UMP9", '(멈칫하며) 에? 어떻게.... ')
scene.addCharacter("HK416_1_dark.png",characterOne  ,characterYCenter )
scene.addCharacter("UMP9_4.png", characterTwo,characterYCenter  )
scenes.append(scene)

scene = Scene("street_dark.png", "HK416", '3분 다 됐어, 아직 안 도망쳤잖아.')
scene.addCharacter("UMP9_4_dark.png", characterTwo,characterYCenter  )
scene.addCharacter("HK416_1.png",characterOne  ,characterYCenter )
scenes.append(scene)

scene = Scene("black.png", "UMP9", '하....♪')
scene.addCharacter("UMP9_2.png", canvasCenterX  ,characterYCenter )
scenes.append(scene)

scene = Scene("black.png", "UMP9", '운이 좋았다고 치지. 이게 마지막 한조각이야, 나와.')
scene.addCharacter("UMP9_2.png", canvasCenterX  ,characterYCenter )
scenes.append(scene)

scene = Scene("black.png", "UMP9", '바로 45 언니한테 연락할테니 일단 어디서 매복해 있어봐.')
scenes.append(scene)

scene = Scene("black.png", "UMP9", '그나저나 철혈의 돌격대가 곧 오는건 진짜라고. 기도라도 하는게 어때?')
scenes.append(scene)

scene = Scene("street_dark.png", "UMP45", 'UMP9 응답하라, 416  그 녀석은 죽었어? ')
scene.addCharacter("Radio3.png", canvasCenterX  ,canvasCenterY )
scenes.append(scene)



############################################################

############################################################
#musicQueue(0, 8, "maintheme.wav")

############################################################
mainScene("street_dark.png")

root.mainloop()