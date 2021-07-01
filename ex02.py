# 일기 예보 프로그램
print('날씨 정보를 입력하세요')
date = input('날짜를 입력하세요(월일)')
day = input('type the day')
mintemp = int(input('type the lowest temperature'))
maxtemp = int(input('type the highest temperature'))
rainprop = int(input('type the chance of raining'))
airrate = input('type the air conditioning')
sunrise = input('type sunrise time')
sunset = input('type sunset time')
southwave = float(input('type 남해앞바다 물결'))
eastwave = float(input('type 동해앞바다 물결'))
westwave = float(input('type 서해앞바다 물결'))

print('-------------------------------')
print('내일 날씨 예보입니다')
print( day + '요일인' + date +'의 아침 최저 기온은' +
      str(mintemp) + '도 , 낮 최고 기온은' + str(maxtemp) + '도로 예보되었습니다')
print('비올 확률은' + str(rainprop) + '이고, 미세먼지는' + airrate + '수준일것으로 예상됩니다')
print('일출시간은' + sunrise + '이고. 일몰시간은' + sunset + '입니다')
print('바다의 물결은 남해 앞바다' + str(southwave) + 'm, 동해앞바다'
      + str(eastwave) + 'm, 서해앞바다' + str(westwave) + 'm ')
print('지금까지 ' + date + '' + day + ' 요일 날씨 예보였습니다 ')

print('-------------------------------')
print('내일 날씨 예보입니다')
print('{0}요일인 {1} 의 아침 최저 기온은 {2}도 , 낮 최고 기온은 {3}도로 예보되었습니다'
      .format(day, date, mintemp, maxtemp))
print('비올 확률은 {0}%이고, 미세먼지는 {1}수준일것으로 예상됩니다'
      .format(rainprop, airrate))
print('일출시간은 {0}이고. 일몰시간은 {1}입니다'
      .format(sunrise, sunset))
print('바다의 물결은 남해 앞바다 {0}m, 동해앞바다 {1}m, 서해앞바다 {2}m '
      .format(southwave,eastwave,westwave))
print('지금까지 {0} {1}요일 날씨 예보였습니다 '
      .format(date, day))

print('-------------------------------')
print('내일 날씨 예보입니다')
print('%s요일인 %s의 아침 최저 기온은 %d도 , 낮 최고 기온은 %d도로 예보되었습니다'
      % (day, date, mintemp, maxtemp))
print('비올 확률은 %d이고, 미세먼지는 %s수준일것으로 예상됩니다'
      % (rainprop, airrate))
print('일출시간은 %s이고. 일몰시간은 %s입니다'
      % (sunrise, sunset))
print('바다의 물결은 남해 앞바다 %fm, 동해앞바다 %fm, 서해앞바다 %fm '
      % (southwave, eastwave, westwave))
print('지금까지 %s %s요일 날씨 예보였습니다 '
      % (date, day))
