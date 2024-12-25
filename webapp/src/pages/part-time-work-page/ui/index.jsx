import {Header} from "../../../widgets/header";
import {CalendarWidget} from "../../../widgets/calendar-widget";
import styles from './styles.module.scss'
import {useState} from "react";
import {TextModal} from "../../../widgets/text-modal";
import {Button} from "../../../widgets/button";

const dates = [
  new Date(2024, 11, 1),
  new Date(2024, 11, 15),
  new Date(2024, 11, 30),
  new Date(2024, 11, 10),
]

const PartTimeWorkPage = () => {
  const [textModalOpen, setTextModalOpen] = useState(true);
  const [selectedDates, setSelectedDates] = useState([]);
  const [elementForTextModal, setElementForTextModal] = useState(
    <p style={{textAlign: "center", width: 231, fontSize: 14}}>
      Выбери желаемые дни для работы, они будут выделяться <span style={{color: '#55C3CD'}}>синим</span>.<br/><br/>Пришлем
      ответ руководителя в чат!
    </p>
  );

  const selectDay = (date) => {
    if (!(!!dates.find((item) => item.getTime() === date.getTime()))) {
      if (!!selectedDates.find((item) => item.getTime() === date.getTime())) {
        setSelectedDates(selectedDates.filter((item) => item.getTime() !== date.getTime()))
      } else {
        setSelectedDates([...selectedDates, date])
      }
    }
  }

  const getTileClassName = (date) => {
    let className = '';
    if (!!dates.find((item) => item.getTime() === date.getTime())) {
      className += styles.day
    } else if (!!selectedDates.find((item) => item.getTime() === date.getTime())) {
      className += styles.choiceDay
    }
    return className
  }

  const onClickButton = () => {
    setElementForTextModal(
      <p style={{ textAlign: "center", width: 236 }}>
        Запрос отправлен! Об ответе оповестим в чате с ботом 🔥
      </p>
    )
    setTextModalOpen(true)
  }

  return (
    <>
      <Header>Выберите смены</Header>
      <CalendarWidget
        className={styles.calendar}
        onClickDay={(date) => selectDay(date)}
        tileClassName={({date}) => getTileClassName(date)}
      />
      <Button onClick={() => onClickButton()} className={styles.button}>подтвердить</Button>
      { textModalOpen && <TextModal setModalOpen={setTextModalOpen}>
        {elementForTextModal}
      </TextModal> }
    </>
  )
}

export default PartTimeWorkPage;
