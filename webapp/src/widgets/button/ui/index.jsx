import styles from './styles.module.scss';

const Button = ({children, onClick}) => {
  return (
    <div
      onClick={() => onClick()}
      className={styles.button}
    >
      {children}
    </div>
  )
}

export default Button;
