import jornada from "../../assets/jornada.png"
import "./styles.css"

const Header = () => {
  return (
    <div className='header-content'>
      <div className="header-logo">
        <img className="logo" src={jornada} alt="/"></img>
        <h1 className="header-h1">Jornada</h1>
      </div>
    </div>
  );
};

export default Header;