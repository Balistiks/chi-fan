import styles from './styles.module.scss'
import TextModal from "../../../widgets/text-modal/ui";
import {useState} from "react";
import {Header} from "../../../widgets/header";
import {Button} from "../../../widgets/button";
import SwitchModal from "../../../widgets/switch-modal/ui";
import axios from "axios";
import {CalendarWidget} from "../../../widgets/calendar-widget";

const dates = [
  new Date(2024, 11, 1),
  new Date(2024, 11, 15),
  new Date(2024, 11, 30),
  new Date(2024, 11, 10),
]

const IndexPage = () => {
  const [date, setDate] = useState(new Date());
  const [textModalOpen, setTextModalOpen] = useState(false)
  const [isSwitch, setIsSwitch] = useState(false);
  const [switchModalOpen, setSwitchModalOpen] = useState(false)
  const [elementForTextModal, setElementForTextModal] = useState(<></>);

  const openShiftModal = (value) => {
    if (!!dates.find((item) => item.getTime() === value.getTime())) {
      setDate(value)
      setElementForTextModal(<p style={{ width: 209 }}>Часы работы: 12:00 - 00:00<br/>Точка: Тихая</p>)
      setTextModalOpen(true)
    }
  }

  const openSwitchModal = (value) => {
    if (!!dates.find((item) => item.getTime() === value.getTime())) {
      setDate(value)
      setSwitchModalOpen(true)
    }
  }

  const onClickEmployee = async () => {
    setSwitchModalOpen(false)
    setElementForTextModal(<p style={{ textAlign: "center", width: 236 }}>Запрос отправлен! Об ответе оповестим в чате с ботом 🔥</p>)
    setTextModalOpen(true)
  }

  return (
    <>
      <Header>{isSwitch ? 'Выберите день' : 'Ваши смены'}</Header>
      <CalendarWidget
        className={styles.calendarHandler}
        onClickDay={(value) => isSwitch ? openSwitchModal(value) : openShiftModal(value)}
        tileClassName={({date}) =>
          !!dates.find((item) => item.getTime() === date.getTime()) ? styles.day : null}
      />
      <Button
        className={styles.button}
        onClick={() => isSwitch ? setIsSwitch(false) : setIsSwitch(true)}
      >
        {isSwitch ? 'мои смены' : 'подмениться'}
      </Button>
      { textModalOpen && <TextModal setModalOpen={setTextModalOpen}>
        {elementForTextModal}
      </TextModal>}
      { switchModalOpen && <SwitchModal onClickEmployee={onClickEmployee} setModalOpen={setSwitchModalOpen}  date={date}/> }
    </>
  )
}

export default IndexPage;
