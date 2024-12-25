import styles from './styles.module.scss';

const Employee = ({width, height, className, onClick}) => {
  return (
    <div onClick={() => onClick()} className={className}>
      <div className={styles.employee} style={{width: width, height: height}}>
        <p className={styles.employee__name}>Кодратьев Никита Станиславович</p>
      </div>
    </div>
  )
}

export default Employee;
