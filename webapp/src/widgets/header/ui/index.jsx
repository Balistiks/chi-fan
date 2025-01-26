import styles from './styles.module.scss'

const Header = ({children}) => {
  return (
    <div className={styles.header}>
      <h1 className={styles.title}>{children}</h1>
    </div>
  )
}

export default Header;
