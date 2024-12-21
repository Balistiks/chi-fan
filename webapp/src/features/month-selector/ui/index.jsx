import styles from './styles.module.scss'

const MonthSelector = ({className}) => {
  return (
    <div className={className}>
      <img src={'icons/arrow left.svg'} alt={'arrow left'}/>
      <p className={styles.month}>декабрь</p>
      <img src={'icons/arrow right.svg'} alt={'arrow right'}/>
    </div>
  )
}

export default MonthSelector;
