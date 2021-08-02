from obspy.imaging.beachball import beachball

# strike, dip, rake
mt = [290.58, 35.49, -88.45]
beachball(mt, size=200, linewidth=2, facecolor='b')
