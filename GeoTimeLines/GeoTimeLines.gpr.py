
register(VIEW,
         id='geotimelines',
         name=_("TimeLines Map"),
         description=_("A view showing all the places visited by a person or persons on various date."),
         version = '1.0.0',
         gramps_target_version='5.2',
         status=STABLE,
         fname='GeoTimeLines.py',
         authors=["Thomas B"],
         authors_email=[""],
         category=("Geography", _("Geography")),
         viewclass='GeoTimeLines',
         icons = [('geo-timelines', _('TimeLines map'))],
         stock_icon='geo-timelines',
         requires_gi=[('OsmGpsMap', '1.0')],
         )
