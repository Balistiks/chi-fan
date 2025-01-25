import styles from './styles.module.scss'
import {useApi} from "../../../shared/lib/hooks/useApi";
import {useEffect} from "react";
import {Employee} from "../../../entities/employee";

const SwitchModal = ({setModalOpen, date, onClickEmployee}) => {
  const tg = window.Telegram.WebApp;
  const {data: schedules, loading: schedulesLoading, fetchData: fetchSchedules} = useApi();

  const fetchData = async () => {
    await fetchSchedules(`schedules/swap/${tg.initDataUnsafe.user.id}/${date.date.toString()}`, 'GET')
  }

  useEffect(() => {
    fetchData()
  }, []);

  const getGroupedSchedules = (schedules) => {
    return schedules.reduce((r, a) => {
      r[`${a.point.name}|${a.startTime.split(':')[0]}:${a.startTime.split(':')[1]} - ${a.endTime.split(':')[0]}:${a.endTime.split(':')[1]}`] = r[`${a.point.name}|${a.startTime.split(':')[0]}:${a.startTime.split(':')[1]} - ${a.endTime.split(':')[0]}:${a.endTime.split(':')[1]}`] || [];
      r[`${a.point.name}|${a.startTime.split(':')[0]}:${a.startTime.split(':')[1]} - ${a.endTime.split(':')[0]}:${a.endTime.split(':')[1]}`].push(a);
      return r;
    }, Object.create(null))
    // return Object.groupBy(
    //   schedules,
    //   ({startTime, endTime, point}) =>
    //     `${point.name}|${startTime.split(':')[0]}:${startTime.split(':')[1]} - ${endTime.split(':')[0]}:${endTime.split(':')[1]}`
    // );
  }

  const getEmployees = () => {
    const groupedSchedules = getGroupedSchedules(schedules)
    const employees = []
    Object.keys(groupedSchedules).forEach((key, value) => {
      employees.push(
        <div key={key}>
          <p className={styles.groupTitle}>
            Часы работы: {key.split('|')[1]} <br/> Точка: {key.split('|')[0]}
          </p>
          {groupedSchedules[key].map((schedule) => (
            <Employee
              key={schedule.id}
              name={schedule.name}
              onClick={async () => await onClickEmployee(date, schedule)}
              className={styles.employee}
              width={'100%'}
              height={28}/>
          ))}
        </div>
      )
    })
    return employees
  }


  return (
    <>
      <div className={styles.darkBg} onClick={() => setModalOpen(false)}/>
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.header}>
            <p>{new Date(date.date).getDate()}</p>
            <p>Выберите коллегу</p>
          </div>
          {!schedulesLoading && (
            <div className={styles.employees}>
              {getEmployees()}
            </div>
          )}
          <div className={styles.exit} onClick={() => setModalOpen(false)}>
            <img src={'/icons/exit.svg'} alt="exit"/>
          </div>
        </div>
      </div>
    </>
  )
}

export default SwitchModal;
