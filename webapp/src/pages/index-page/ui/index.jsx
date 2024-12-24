import Calendar from 'react-calendar';
import './calendar.css'
import styles from './styles.module.scss'
import ShiftDayModal from "../../../widgets/shift-day-modal/ui";
import {useState} from "react";

const dates = [
  new Date(2024, 11, 1),
  new Date(2024, 11, 15),
  new Date(2024, 11, 30),
  new Date(2024, 11, 10),
]

const IndexPage = () => {
  const [date, setDate] = useState(new Date());
  const [modalOpen, setModalOpen] = useState(false)

  return (
    <>
      <div className={styles.calendarHandler}>
        <Calendar
          onChange={null}
          className={styles.calendar}
          onClickMonth={null}
          minDetail={'month'}
          nextLabel={<img src={'/icons/arrow right.svg'} alt={'arrow right'}/>}
          prevLabel={<img src={'/icons/arrow left.svg'} alt={'arrow left'}/>}
          onClickDay={(value) => {
            if (!!dates.find((item) => item.getTime() === value.getTime())) {
              setDate(value)
              setModalOpen(true)
            }
          }}
          tileClassName={({ date, view }) =>
            !!dates.find((item) => item.getTime() === date.getTime()) ? styles.day : null}
        />
        { modalOpen && <ShiftDayModal setModalOpen={setModalOpen} /> }
      </div>
    </>
  )
}

export default IndexPage;
