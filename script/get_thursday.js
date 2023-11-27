function getLastThursday(date) {
  // 지난 주 목요일을 구하기 위해 현재 요일과 날짜를 가져옵니다.
  let dayOfWeek = date.getDay();
  let dayOfMonth = date.getDate();
  console.log(dayOfMonth);

  // 만약 오늘이 목요일 이전이면, 일주일 전 목요일을 구합니다.
  if (dayOfWeek < 4) {
    return new Date(
      date.getFullYear(),
      date.getMonth(),
      dayOfMonth - (dayOfWeek + 7 - 4)
    );
  }
  // 오늘이 목요일 이후이면, 이번 주 목요일이 아니라 지난 주 목요일을 구해야 합니다.
  else {
    return new Date(
      date.getFullYear(),
      date.getMonth(),
      dayOfMonth - (dayOfWeek - 4)
    );
  }
}

function test() {
  let today = new Date();
  let lastWeek = new Date();
  lastWeek.setDate(today.getDate() - 7);
  while (lastWeek.getDay() !== 4) {
    lastWeek.setDate(lastWeek.getDate() + 1);
  }
  let lastThursday = lastWeek.toLocaleDateString();
  console.log(lastThursday);
  return lastThursday;
}

function month_window() {
  //window.open('https://www.weather.go.kr/w/weather/long-term/month1.do#','1개월전망','width =900px, height=900px, top=50%, left=50%, location = no, status=no, scrollbars=yes' )

  temp_url =
    'https://www.weather.go.kr/w/repositary/xml/fct/mon/fct_mon1_133_' +
    test() +
    '.pdf';
  console.log(temp_url);
  window.open(
    temp_url,
    '1개월전망',
    'width =900px, height=900px, top=50%, left=50%, location = no, status=no, scrollbars=yes'
  );
}
