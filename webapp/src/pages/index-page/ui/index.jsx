import styles from './styles.module.scss'
import TextModal from "../../../widgets/text-modal/ui";
import {useEffect, useState} from "react";
import {Header} from "../../../widgets/header";
import {Button} from "../../../widgets/button";
import SwitchModal from "../../../widgets/switch-modal/ui";
import {CalendarWidget} from "../../../widgets/calendar-widget";
import {useApi} from "../../../shared/lib/hooks/useApi.js";
import axios from 'axios'
import {token, WEB_URL} from "../../../shared/config";

const IndexPage = () => {
  const tg = window.Telegram.WebApp;

  const [date, setDate] = useState({});
  const [textModalOpen, setTextModalOpen] = useState(false)
  const [isSwitch, setIsSwitch] = useState(false);
  const [switchModalOpen, setSwitchModalOpen] = useState(false)
  const [elementForTextModal, setElementForTextModal] = useState(<></>);

  const {data: schedules, loading: schedulesLoading, fetchData: fetchSchedules} = useApi();

  const openShiftModal = (value) => {
    const schedule = schedules.find((item) =>
      new Date(item.date).setHours(0, 0, 0) === value.getTime())
    if (schedule) {
      setDate(schedule)
      const startTime = `${schedule.startTime.split(':')[0]}:${schedule.startTime.split(':')[1]}`
      const endTime = `${schedule.endTime.split(':')[0]}:${schedule.endTime.split(':')[1]}`
      setElementForTextModal(
        <p style={{ width: 209 }}>Часы работы: {startTime} - {endTime}<br/>Точка: {schedule.point.name}</p>
      )
      setTextModalOpen(true)
    }
  }

  const openSwitchModal = async (value) => {
    const schedule = schedules.find((item) =>
      new Date(item.date).setHours(0, 0, 0) === value.getTime())
    if (schedule) {
      setDate(schedule)
      setSwitchModalOpen(true)
    }
  }

  const onClickEmployee = async (mainSchedule, scheduleForSwap) => {
    setSwitchModalOpen(false)
    await axios.post(`${WEB_URL}/users/date`, {
      mainSchedule: mainSchedule,
      scheduleForSwap: scheduleForSwap,
    }, { headers: { 'Authorization': `Bearer ${token}` }})
    setElementForTextModal(<p style={{ textAlign: "center", width: 236 }}>Запрос отправлен! Об ответе оповестим в чате с ботом 🔥</p>)
    setTextModalOpen(true)
  }

  useEffect(() => {
    fetchData()
  }, []);

  const fetchData = async () => {
    try {
      await fetchSchedules(`schedules?tgId=${tg.initDataUnsafe.user.id}`, 'GET')
    } catch (e) {
      console.log(e)
    }
  }

  return (
    <>
      <Header>{isSwitch ? 'Выберите день' : 'Ваши смены'}</Header>
      { !schedulesLoading &&  (
        <CalendarWidget
          className={styles.calendarHandler}
          onClickDay={(value) => isSwitch ? openSwitchModal(value) : openShiftModal(value)}
          tileClassName={({date}) => schedules !== undefined ? !!schedules.find((item) =>
            new Date(item.date).setHours(0, 0, 0) === date.getTime()) ? styles.day : null : null
          }
        />
      )}
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
