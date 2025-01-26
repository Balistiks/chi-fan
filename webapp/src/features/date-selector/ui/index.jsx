const DateSelector = ({startDate, endDate, startDayOfWeek, weeksCount}) => {
  const days = [[]]

  for (let i = 0; i < (startDayOfWeek === 0 ? 7 : startDayOfWeek) - 1; i++) {
    days[0].push(null)
  }

  console.log(weeksCount)

  return (
    <div>

    </div>
  )
}

export default DateSelector;
