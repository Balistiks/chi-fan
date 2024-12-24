import styles from './styles.module.scss';

const ShiftDayModal = ({setModalOpen}) => {
  return (
    <>
      <div className={styles.darkBg} onClick={() => setModalOpen(false)}/>
      <div className={styles.centered}>
        <div className={styles.modal}>
          <p>Часы работы: 12:00 - 00:00<br/>Точка: Тихая</p>
          <div className={styles.exit} onClick={() => setModalOpen(false)}>
            <img src={'/icons/exit.svg'} alt="exit"/>
          </div>
        </div>
      </div>
    </>
  )
}

export default ShiftDayModal;
