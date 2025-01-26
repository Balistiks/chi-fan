import './calendar.css'
import Calendar from "react-calendar";

const CalendarWidget = ({onClickDay, tileClassName, className}) => {
  return (
    <div className={className}>
      <Calendar
        minDetail={'month'}
        nextLabel={<img src={'/icons/arrow right.svg'} alt={'arrow right'}/>}
        prevLabel={<img src={'/icons/arrow left.svg'} alt={'arrow left'}/>}
        onClickDay={(value) => onClickDay(value)}
        tileClassName={(data) => tileClassName(data)}
      />
    </div>
  )
}

export default CalendarWidget;
