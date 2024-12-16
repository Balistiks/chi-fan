import {Route, Routes} from "react-router";

const pagesRoutes = {
  index: '/',
  indexExternal: '/external',
  externalCoursePage: '/external/course/:id',
  vacancy: '/vacancy/:id'
}

const pages = [
  {path: pagesRoutes.index, component: <IndexPage/>, exact: true},
]

const Routing = () => {
  return (
    <Routes>
      {pages.map((route) => (
        <Route
          element={route.component}
          path={route.path}
          exact={route.exact}
          key={route.path}
        />
      ))}
    </Routes>
  )
}

export default Routing;
