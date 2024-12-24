import {MonthSelector} from "../../../features/month-selector";
import styles from './styles.module.scss'
import {DateSelector} from "../../../features/date-selector";
import {useState} from "react";
import {eachWeekOfInterval, endOfMonth, startOfMonth} from "date-fns";

const Calendar = () => {
  const [date, setDate] = useState(new Date());

  const changeMonth = (add) => {
    setDate(new Date(date.setMonth(date.getMonth() + add)))
  }

  return (
    <div className={styles.calendar}>
      <MonthSelector
        className={styles.monthSelector}
        month={date.toLocaleString('ru', { month: "long" })}
        changeMonth={changeMonth}
      />
      <DateSelector
        startDate={startOfMonth(date).getDate()}
        endDate={endOfMonth(date).getDate()}
        startDayOfWeek={startOfMonth(date).getDay()}
        weeksCount={eachWeekOfInterval({
          start: startOfMonth(date),
          end: endOfMonth(date)
        })}
      />
    </div>
  )
}

export default Calendar;
