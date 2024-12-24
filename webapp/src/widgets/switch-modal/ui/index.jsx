import styles from './styles.module.scss'
import Employee from "../../../entities/employee/ui";
const SwitchModal = ({setModalOpen, date}) => {
  return (
    <>
      <div className={styles.darkBg} onClick={() => setModalOpen(false)}/>
      <div className={styles.centered}>
        <div className={styles.modal}>
          <div className={styles.header}>
            <p>{date.getDate()}</p>
            <p>Выберите коллегу</p>
          </div>
          <div className={styles.employees}>
            <Employee className={styles.employee} width={'100%'} height={28}/>
            <Employee className={styles.employee} width={'100%'} height={28}/>
            <Employee className={styles.employee} width={'100%'} height={28}/>
            <Employee className={styles.employee} width={'100%'} height={28}/>
            <Employee className={styles.employee} width={'100%'} height={28}/>
            <Employee className={styles.employee} width={'100%'} height={28}/>
            <Employee className={styles.employee} width={'100%'} height={28}/>
            <Employee className={styles.employee} width={'100%'} height={28}/>
          </div>
          <div className={styles.exit} onClick={() => setModalOpen(false)}>
            <img src={'/icons/exit.svg'} alt="exit"/>
          </div>
        </div>
      </div>
    </>
  )
}

export default SwitchModal;
