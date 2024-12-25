import styles from './styles.module.scss';

const TextModal = ({setModalOpen, children}) => {
  return (
    <>
      <div className={styles.darkBg} onClick={() => setModalOpen(false)}/>
      <div className={styles.centered}>
        <div className={styles.modal}>
          {children}
          <div className={styles.exit} onClick={() => setModalOpen(false)}>
            <img src={'/icons/exit.svg'} alt="exit"/>
          </div>
        </div>
      </div>
    </>
  )
}

export default TextModal;
