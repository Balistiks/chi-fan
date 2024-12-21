import {MonthSelector} from "../../../features/month-selector";
import styles from './styles.module.scss'
import {DateSelector} from "../../../features/date-selector";

const Calendar = () => {
  return (
    <div className={styles.calendar}>
      <MonthSelector className={styles.monthSelector} />
      <DateSelector />
    </div>
  )
}

export default Calendar;
