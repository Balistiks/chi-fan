import Calendar from 'react-calendar';
import './calendar.css'
import styles from './styles.module.scss'
import ShiftDayModal from "../../../widgets/shift-day-modal/ui";
import {useState} from "react";
import {Header} from "../../../widgets/header";
import {Button} from "../../../widgets/button";
import SwitchModal from "../../../widgets/switch-modal/ui";

const dates = [
  new Date(2024, 11, 1),
  new Date(2024, 11, 15),
  new Date(2024, 11, 30),
  new Date(2024, 11, 10),
]

const IndexPage = () => {
  const [date, setDate] = useState(new Date());
  const [shiftModalOpen, setShiftModalOpen] = useState(false)
  const [isSwitch, setIsSwitch] = useState(false);
  const [switchModalOpen, setSwitchModalOpen] = useState(false)

  const openShiftModal = (value) => {
    if (!!dates.find((item) => item.getTime() === value.getTime())) {
      setDate(value)
      setShiftModalOpen(true)
    }
  }

  const openSwitchModal = (value) => {
    if (!!dates.find((item) => item.getTime() === value.getTime())) {
      setDate(value)
      setSwitchModalOpen(true)
    }
  }

  return (
    <div className={styles.indexPage}>
      <Header>{isSwitch ? 'Выберите день' : 'Ваши смены'}</Header>
      <div className={styles.calendarHandler}>
        <Calendar
          onChange={null}
          onClickMonth={null}
          minDetail={'month'}
          nextLabel={<img src={'/icons/arrow right.svg'} alt={'arrow right'}/>}
          prevLabel={<img src={'/icons/arrow left.svg'} alt={'arrow left'}/>}
          onClickDay={(value) => isSwitch ? openSwitchModal(value) : openShiftModal(value)}
          tileClassName={({ date }) =>
            !!dates.find((item) => item.getTime() === date.getTime()) ? styles.day : null}
        />
        { shiftModalOpen && <ShiftDayModal setModalOpen={setShiftModalOpen} /> }
      </div>
      <Button
        onClick={() => isSwitch ? setIsSwitch(false) : setIsSwitch(true)}
      >
        {isSwitch ? 'мои смены' : 'подмениться'}
      </Button>
      { switchModalOpen && <SwitchModal setModalOpen={setSwitchModalOpen}  date={date}/> }
    </div>
  )
}

export default IndexPage;
