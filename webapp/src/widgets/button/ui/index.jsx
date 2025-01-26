import styles from './styles.module.scss';

const Button = ({children, onClick, className}) => {
  return (
    <div className={className}>
      <div
        onClick={() => onClick()}
        className={styles.button}
      >
        {children}
      </div>
    </div>
  )
}

export default Button;
