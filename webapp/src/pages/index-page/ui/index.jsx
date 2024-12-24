import Calendar from 'react-calendar';
import './calendar.css'
import styles from './styles.module.scss'
import ShiftDayModal from "../../../widgets/shift-day-modal/ui";
import {useState} from "react";

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
            setDate(value)
            setModalOpen(true)
          }}
        />
        { modalOpen && <ShiftDayModal setModalOpen={setModalOpen} /> }
      </div>
    </>
  )
}

export default IndexPage;
