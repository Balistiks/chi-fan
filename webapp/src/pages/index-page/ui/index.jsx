import Calendar from 'react-calendar';
import './calendar.css'
import styles from './styles.module.scss'

const IndexPage = () => {
  return (
    <>
      <div className={styles.calendarHandler}>
        <Calendar
          className={styles.calendar}
          onClickMonth={null}
          minDetail={'month'}
          nextLabel={<img src={'/icons/arrow right.svg'} alt={'arrow right'}/>}
          prevLabel={<img src={'/icons/arrow left.svg'} alt={'arrow left'}/>}
        />
      </div>
    </>
  )
}

export default IndexPage;
