import * as React from 'react';
import {Suspense} from "react";
import {createBrowserRouter, RouterProvider} from "react-router";
import {IndexPage} from "../pages/index-page";
import './styles/normalizez.scss'
import './styles/reset.scss'
import './styles/fonts.scss'
import {PartTimeWorkPage} from "../pages/part-time-work-page";
import './styles/styes.scss'

const router = createBrowserRouter([
  {
    path: '/',
    element: <IndexPage />
  },
  {
    path: '/part-time-work',
    element: <PartTimeWorkPage />
  }
])

const App = () => {
  return (
    <>
      <Suspense fallback={<p>Загрузка...</p>}>
        <RouterProvider router={router} />
      </Suspense>
    </>
  )
}

export default App;
