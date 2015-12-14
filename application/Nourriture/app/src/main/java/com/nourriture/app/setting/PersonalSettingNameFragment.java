package com.nourriture.app.setting;

import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import com.nourriture.app.R;

/**
 * Created by liuyifan on 15/12/10.
 */
public class PersonalSettingNameFragment extends Fragment {
    private View view;
    private String name;
    boolean isTwoPane;

    @Override
    public void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);

        //get name and isTwoPane from Bundle--tablet or Intent--phone
        if (getArguments()!=null && getArguments().containsKey("name") && getArguments().containsKey("isTwoPane")) {
            name = getArguments().getString("name");
            isTwoPane = getArguments().getBoolean("isTwoPane");
        } else if (getActivity().getIntent().getStringExtra("name") != null) {
            name = getActivity().getIntent().getStringExtra("name");
            isTwoPane = getActivity().getIntent().getBooleanExtra("isTwoPane", false);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        view = inflater.inflate(R.layout.setting_name_frag, container, false);

        EditText nameView = (EditText) view.findViewById(R.id.edit_name);
        nameView.setText(name);

        Button button = (Button) view.findViewById(R.id.name_submit);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view1) {
                EditText editText = (EditText) view.findViewById(R.id.edit_name);
                String new_name = editText.getText().toString();

                if (!name.equals(new_name)) {
                    if (isTwoPane) {
                        // refresh the value of name in the left fragment
                        PersonalSettingFragment personalSettingFragment = (PersonalSettingFragment)
                                getActivity().getSupportFragmentManager().getFragments().get(0); //maybe there is a better way to get the fragmant
                        personalSettingFragment.changeValue(0, new_name);
                    } else {
                        // return the value of name to PersonalSettingFragment
                        Intent intent = getActivity().getIntent();
                        intent.putExtra("name", new_name);
                        getActivity().setResult(0, intent);
                        getActivity().finish();
                    }
                    name = new_name;
                }
            }
        });
        return view;
    }
}
