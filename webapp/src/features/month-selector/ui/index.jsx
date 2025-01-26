import styles from './styles.module.scss'

const MonthSelector = ({className, month, changeMonth}) => {
  const onClickHandler = (add) => {
    changeMonth(add)
  }

  return (
    <div className={className}>
      <img
        src={'icons/arrow left.svg'}
        alt={'arrow left'}
        onClick={() => onClickHandler(-1)}
      />
      <p className={styles.month}>{month}</p>
      <img
        src={'icons/arrow right.svg'}
        alt={'arrow right'}
        onClick={() => onClickHandler(1)}
      />
    </div>
  )
}

export default MonthSelector;
