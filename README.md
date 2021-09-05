# url-shortener-app
[![Last Commit](https://img.shields.io/github/last-commit/joash-jw/url-shortener-app)]()

This web application converts a long URL when input and provide a short URL. For example:

:heavy_exclamation_mark: Long URL: https://www.amazon.sg/b/ref=shvl_desk1_elec?ie=UTF8&node=6314449051&pf_rd_r=ECAAM3PXCEARPXM0TJ78&pf_rd_p=0e068dd1-5d48-408b-886f-6f6001062463&pd_rd_r=4b4934a5-6976-449b-91fc-bef3270268ab&pd_rd_w=FsOAo&pd_rd_wg=HHurM&ref_=pd_gw_unk

:white_check_mark: Short URL: http://{`hostname`}:{`port`}/123456

Upon entering the short URL, the user will be directed back to their previously input long URL.

## Technical Information
To run the app:
```shell
python app.py
```

To run unit test:
```shell
python -m unittest discover -p test.py
```